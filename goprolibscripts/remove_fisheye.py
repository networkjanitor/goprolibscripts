import goprolib.HERO4.fisheye as H4LC
import os
import os.path
import wand.image
import wand.exceptions


def remove_fisheye_from_directory(input_path, output_path, lens_correction_set, parse_subdirectories=False):
    allfiles = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f)) and not os.path.isfile(os.path.join(output_path, f))
                and f != 'leinfo.sav']

    try:
        os.makedirs(output_path)
    except FileExistsError:
        pass

    if parse_subdirectories:
        alldirectories = [f for f in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, f))
                          and os.path.join(input_path, f) != output_path
                          and os.path.join(input_path, f) + '/' != output_path]
        for dir in alldirectories:
            remove_fisheye_from_directory(os.path.join(input_path, dir), os.path.join(output_path, dir), lens_correction_set,
                                          parse_subdirectories)

    for file in allfiles:
        remove_fisheye_from_file(os.path.join(input_path,file), os.path.join(output_path,file), lens_correction_set)


def remove_fisheye_from_file(input_path, output_path, lens_correction_set):
    print(input_path)
    try:
        with wand.image.Image(filename=input_path) as img:
            img.distort(method='barrel', arguments=lens_correction_set)
            img.save(filename=output_path)
    except wand.exceptions.WandException as e:
        print(e)

    print()


def main():
    remove_fisheye_from_directory('/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/',
                                  '/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/lenscorrected/',
                                  [0.06335, -0.18432, -0.13009], parse_subdirectories=True)


if __name__ == '__main__':
    while True:
        main()


        # remove_fisheye_from_file('/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_13 GoPro Auto/101GOPRO/G0082567.JPG', [0.06335, -0.18432, -0.13009])
