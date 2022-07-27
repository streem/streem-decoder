## Proto messages

These are the protobuf message schemas for `pbmesh` and `pblayout`

**NOTE:** Not for compiling. This is just for documentation purpose only. DO NOT build with these proto definitions. 

------  

```
message Mesh {
    VectorBuffer vertices = 1;
    // Currently, a `face` is a derived from a triangle. So each `face` will consist of 3 components.
    VectorBuffer faces = 2;
    VectorBuffer normals = 3;
    // `face_classifications` is an enum, see: https://developer.apple.com/documentation/arkit/armeshclassification
    // and currently is 1 component per vector.
    // Each `face` in faces will have one of `face_classification` in this list.
    // Meaning for every `face` there will be 3 components to
    // every 1 component of `face_classifications`.
    VectorBuffer face_classifications = 4;
    Platform platform = 5;

    enum Platform {
        PLATFORM_INVALID = 0;
        PLATFORM_IOS = 1;
        PLATFORM_ANDROID = 2;
    }
}

message VectorBuffer {
    bytes bytes = 1; // The bytes of your buffer
    int32 offset = 2; // The offset in bytes for when your data starts in your buffer
    ComponentType component_type = 3; // The data type of your bytes
    int32 component_stride = 4; // The length, in bytes, of the start of one component within a vector to the start of the next component
    int32 components_per_vector = 5; // How many components make up each vector in your buffer
    int32 vector_stride = 6; // The length, in bytes, of the start of one vector in the buffer to the start of the next vector
    int32 vector_count = 7; // How many vectors are in your buffer
    ByteOrder byte_order = 8; // How bytes are ordered in each component

    enum ComponentType {
        COMPONENT_TYPE_INVALID = 0;
        COMPONENT_TYPE_FLOAT = 1;
        COMPONENT_TYPE_DOUBLE = 2;
        COMPONENT_TYPE_UINT32 = 3;
        COMPONENT_TYPE_UINT8 = 4;
        COMPONENT_TYPE_UINT16 = 5;
    }

    enum ByteOrder {
        BYTE_ORDER_INVALID = 0;
        BYTE_ORDER_BIG_ENDIAN = 1;
        BYTE_ORDER_LITTLE_ENDIAN = 2;
    }
}

// pblayout message
message LayoutEstimationData {
    VectorBuffer layout_edge_vertices = 1;
    Mesh triangulated_floor = 2;
    float area_square_meters = 3;
}

message Size {
    float width = 1;
    float height = 2;
}

message Pose {
    // position: x,y,z in meters
    repeated float position = 1;
    // rotation: either x,y,z Euler angles in degrees,
    //           or else x,y,z,w as a quaternion
    repeated float rotation = 2;
}

message CameraIntrinsics {
    float focal_length_px_x = 1;
    float focal_length_px_y = 2;
    float axis_skew = 3;
    float principal_point_x = 4;
    float principal_point_y = 5;
}

//pbmesh message
message MeshArtifact {
    // Includes one or more trackables of type Mesh,
    // and zero or more trackables of type Plane.
    repeated streem.room.ar.Trackable trackables = 1;
    // Texture for the Mesh
    repeated Enhancement mesh_enhancements = 2;

    message Enhancement {
        bytes texture_jpeg_data = 1;
        CameraIntrinsics camera_intrinsics = 2;
        streem.api.Size camera_dimensions = 3;
        streem.api.Pose camera_pose = 4;
    }
}

message Trackable {
    bytes id = 1;

    // The trackable's pose in the world coordinate space.
    streem.api.Pose pose = 2;

    oneof type {
        Mesh mesh = 105;
    }
}
```