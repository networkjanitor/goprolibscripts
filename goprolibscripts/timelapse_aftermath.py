import subprocess
import os
import os.path
import re

def check_output_dir(output_path):
    try:
        os.makedirs(output_path)
    except FileExistsError:
        pass

def morph_directory(input_path, output_path, number_of_added_frames, input_filename_pattern='*', output_filename_pattern=''):
    check_output_dir(output_path)
    env = os.environ.copy()
    env['MAGICK_TEMPORARY_PATH'] = '/media/xyoz/XYOZ-INT1000E/tmp'
    params = ['convert', '-verbose','-morph', str(number_of_added_frames), os.path.join(input_path,input_filename_pattern), os.path.join(output_path, output_filename_pattern)]
    try:
        result = subprocess.check_call(params, env=env)
        print(result)
    except subprocess.CalledProcessError as a:
        print(a)

def rename_in_dictionary(source_path, input_pattern, output_pattern='{}.JPG'):
    allfiles = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f)) and re.fullmatch(input_pattern, f) is not None]
    for index, file in enumerate(allfiles):
        os.rename(os.path.join(source_path,file), os.path.join(source_path,output_pattern.format(file[1:])))


def create_video(input_path, output_path):
    check_output_dir(output_path)
    params = []
    subprocess.call(params)

def main():
    morph_directory('/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/102GOPRO',
                    '/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/morph_result/', 1,
                    output_filename_pattern='.JPG')


if __name__ == '__main__':
    rename_in_dictionary('/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/morph_result/', '.*')
