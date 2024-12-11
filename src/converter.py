def convert_tom_to_obj(tom_file, obj_file):
    try:
        with open(tom_file, 'r') as tom, open(obj_file, 'w') as obj:
            vertices = []
            faces = []
            for line in tom:
                parts = line.strip().split()
                if parts[0] == "vertex":
                    # Assuming "vertex x y z" format in .tom
                    x, y, z = map(float, parts[1:])
                    vertices.append(f"v {x} {y} {z}\n")
                elif parts[0] == "face":
                    # Assuming "face v1 v2 v3" format in .tom
                    face_indices = " ".join(parts[1:])
                    faces.append(f"f {face_indices}\n")

            # Write vertices to .obj
            obj.writelines(vertices)
            # Write faces to .obj
            obj.writelines(faces)

        print(f"Conversion completed: {obj_file}")

    except Exception as e:
        print(f"Error: {e}")


# Run the converter
if __name__ == "__main__":
    tom_path = "data/sample.tom"  # Input file path
    obj_path = "data/converted_model.obj"  # Output file path
    convert_tom_to_obj(tom_path, obj_path)

