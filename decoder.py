import numpy as np
from streem.room.ar import storage_pb2
from streem.room import rooms_pb2
from scipy.spatial.transform import Rotation as R
import trimesh
import argparse


parser = argparse.ArgumentParser(description='Streem proto message decoder')
parser.add_argument('--input-mesh', dest='input_pbmesh', 
                    default="data/mesh_1618312522461.pbmesh",
                    type=str, help='Location of the input pbmesh file (defaults to pbmesh file in data folder)')
parser.add_argument('--output-mesh', dest='output_obj',
                    default="data/test.obj",
                    type=str, help='Location of the output obj file to export (defaults to test.obj in data folder)')
parser.add_argument('--input-pblayout', dest='input_pblayout', 
                    default="data/layout_estimation.pblayout",
                    type=str, help='Location of the input pblayout file (defaults to pblayout file in data folder)')

def get_dtype(component_type):
    if (component_type == rooms_pb2.VectorBuffer.COMPONENT_TYPE_UINT32):
        return np.uint32
    elif (component_type == rooms_pb2.VectorBuffer.COMPONENT_TYPE_FLOAT):
        return np.float32
    elif (component_type == rooms_pb2.VectorBuffer.COMPONENT_TYPE_DOUBLE):
        return np.float64
    elif (component_type == rooms_pb2.VectorBuffer.COMPONENT_TYPE_UINT8):
        return np.uint8
    elif (component_type == rooms_pb2.VectorBuffer.COMPONENT_TYPE_UINT16):
        return np.uint16
    elif (component_type == rooms_pb2.VectorBuffer.COMPONENT_TYPE_INVALID):
        raise Exception("Invalid vector buffer component type!")
    else:
        raise Exception("Unknown vector buffer component type!")

def get_nparray_from_vector_buffer(vector_buffer):
    np_array = np.frombuffer(vector_buffer.bytes,
                             dtype=get_dtype(vector_buffer.component_type),
                             offset=vector_buffer.offset,
                             count=-1)
    shape =  (vector_buffer.vector_count, vector_buffer.components_per_vector)     
    strides = (vector_buffer.vector_stride,vector_buffer.component_stride)                         
    np_array = np.lib.stride_tricks.as_strided(np_array, shape, strides)

    return np_array

def decode_pbmesh(pbmesh_bytes):
    mesh_artifact = storage_pb2.MeshArtifact()
    mesh_artifact.ParseFromString(pbmesh_bytes)

    total_vertices = np.empty(shape=(0, 3))
    total_faces = np.empty(shape=(0, 3))
    total_normals = np.empty(shape=(0, 3))

    for idx, trackable in enumerate(mesh_artifact.trackables):

        mesh_buffer = trackable.mesh
        anchor_pose = trackable.pose

        if mesh_buffer.vertices.vector_count == 0:
            continue

        vertices = get_nparray_from_vector_buffer(mesh_buffer.vertices)

        if len(anchor_pose.rotation) != 0:
            r = np.eye(3)
            if len(anchor_pose.rotation) == 3:
                r = R.from_euler(anchor_pose.rotation)
            if len(anchor_pose.rotation) == 4:
                r = R.from_quat(anchor_pose.rotation)
            else:
                raise Exception("Invalid rotation vector length!")
            vertices = np.dot(vertices, np.transpose(r.as_matrix()))
        if len(anchor_pose.position) != 0:
            vertices = vertices + anchor_pose.position

        total_vertices = np.concatenate((total_vertices, vertices))

        if mesh_buffer.normals.vector_count > 0:
            normals = get_nparray_from_vector_buffer(mesh_buffer.normals)

            total_normals = np.concatenate((total_normals, normals))

        if mesh_buffer.faces.vector_count > 0:
            faces = get_nparray_from_vector_buffer(mesh_buffer.faces)
            faces = faces + len(total_vertices) - len(vertices)
            total_faces = np.concatenate((total_faces, faces))

    components = {"vertices": total_vertices,
                  "normals": total_normals,
                  "faces": total_faces}
    return components

def getbytes_pb(pb_file):
    pb_bytes = b''
    with open(pb_file, "rb") as f:
        pb_bytes = f.read()
    return pb_bytes

def decode_pbmesh_to_obj(pb_mesh_file_path, obj_path):

    pbmesh_bytes = getbytes_pb(pb_mesh_file_path)
    mesh_components = decode_pbmesh(pbmesh_bytes)

    mesh_t = trimesh.Trimesh(vertices=mesh_components['vertices'].tolist(),
                       faces=mesh_components['faces'].tolist(),
                    normals=mesh_components['normals'].tolist())
    with open(obj_path, 'w', encoding='utf-8') as f:
        mesh_t.export(f, file_type='obj')
    print(f"Exported mesh to {obj_path}")

def decode_pblayout(pb_layout_file_path):

    pblayout_bytes = getbytes_pb(pb_layout_file_path)
    layout_estimation_data = storage_pb2.LayoutEstimationData()
    layout_estimation_data.ParseFromString(pblayout_bytes)
    vertices = get_nparray_from_vector_buffer(layout_estimation_data.layout_edge_vertices)
    print(f"Vertices - {vertices}")
    print(f"Layout area - {layout_estimation_data.area_square_meters}")

if __name__ == "__main__":

    args = parser.parse_args()
    decode_pbmesh_to_obj(args.input_pbmesh, args.output_obj)
    decode_pblayout(args.input_pblayout)