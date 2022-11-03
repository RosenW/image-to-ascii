#!/usr/bin/python

import sys

image_path_index = 1;

if image_path_index < len(sys.argv):
    # TODO Version 1: Read bytes
    # Check if BMP - first 2 bytes are 'BM' (in Hex: 424D) OK
    # Get Width and Height OK
    # Parse value array OK
    # Compress bytes so image fits NO
    # Define illumination OK
    # Iterate bytes and draw the image OK
    # Create adequate error handling NO

    file_path = sys.argv[image_path_index];

    with open(file_path, "rb") as f:
        # Check if BMP - first 2 bytes are 'BM' (in Hex: 424D)
        byte_chunk = f.read(2);
        if byte_chunk != b"BM":
            # TODO: Throw error, stop execution
            print("Error: Image format not supported, supported image formats: [ BMP ]");
        else:
            print(byte_chunk);


        # TODO: Use Constants
        # Get to pixel array offset info
        f.seek(10);
        pixel_array_offset = int.from_bytes(f.read(4), 'little');

        # Size offset:
        f.seek(18);
        width  = int.from_bytes(f.read(4), 'little');
        height = int.from_bytes(f.read(4), 'little');

        print(width);
        print(height);

        # Get to pixel array
        f.seek(pixel_array_offset);

        # pixel is represented by 4 bytes - BLUE GREEN RED ALPHA (0 - 255)
        byte_chunk = b"!";

        image = [];
        illumination_arr = ['.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@'];
        max_value = 255;
        illumination_mod = max_value / len(illumination_arr);

        for pixel_num in range(0, width * height):
            byte_chunk = f.read(1);

            # TODO: Parse bytes per pixel value and use it
            # TODO: Assert if you cant handle bytes per pixel
            illumination_value = (byte_chunk[0]);

            image.append(illumination_arr[round(illumination_value / illumination_mod) - 1]);

            if pixel_num % (width + 1) == 0:
                image.append("\n");

        for pixel in reversed(image):
            print(pixel, end='');

else:
    print("Error: No image provided. an image can be passed as the first parameter 'python3 script_name.py <image_path>'");
