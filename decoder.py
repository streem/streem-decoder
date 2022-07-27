import numpy as np
from streem.room.ar import storage_pb2
from streem.room import rooms_pb2
from scipy.spatial.transform import Rotation as R
import trimesh

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
                             count=vector_buffer.vector_count
                                   * vector_buffer.components_per_vector)
    count = vector_buffer.vector_count
    np_array = np_array.reshape(
        (count, vector_buffer.components_per_vector))

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
            r = R.from_quat(anchor_pose.rotation)
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

def decode_pblayout(pb_layout_file_path):

    pblayout_bytes = getbytes_pb(pb_layout_file_path)
    layout_estimation_data = storage_pb2.LayoutEstimationData()
    layout_estimation_data.ParseFromString(pblayout_bytes)

    print(layout_estimation_data.area_square_meters)

mesh = decode_pbmesh_to_obj("mesh_1618312522461.pbmesh", "test.obj")
decode_pblayout("layout_estimation.pblayout")