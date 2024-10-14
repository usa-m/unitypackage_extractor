from os      import listdir, mkdir
from os.path import isdir, isfile, join
from unitypackage_extractor.extractor import extractPackage

SCAN_DIR = r"D:\UnityAssets"
OUT_DIR = r"D:\UnityAssets\[ExtractedAssets]"
EN_SEPARATE_FOLDERS = True

# Creating output directory
if not isdir(OUT_DIR):
  mkdir(OUT_DIR)

# Enlisting directories
def get_dirs(start_dir, depth = 0):
  try:
    if isdir(start_dir):
      yield start_dir
      
      for name in listdir(start_dir):
        full_name = join(start_dir, name)
        
        if isdir(full_name):
           yield full_name
        
        if depth > 0:
           yield from get_dirs(full_name, depth - 1)
  except:
    pass # cannot access - {start_dir}

# Enlisting files
def get_files_in_dir(dir_name, extension = ""):
  try:
    for name in listdir(dir_name):
      full_name = join(dir_name, name)

      if isfile(full_name):
        if extension == None or \
           extension == "" or   \
           name.lower().endswith(extension.lower()):
          yield (full_name, name)

  except:
      return f"<cannot access - {dir_name}>"

# Processing all the Unity Package files
file_count = 0
output_path = OUT_DIR
for scan_dirname in get_dirs(SCAN_DIR, depth = 20):
  for (scan_file_path, scan_filename) in get_files_in_dir(scan_dirname, ".unitypackage"):
    file_count += 1

    print(f"Processing (#{file_count}) -- {scan_file_path}")
    
    if EN_SEPARATE_FOLDERS:
      output_path = join(OUT_DIR, scan_filename)

    extractPackage(scan_file_path, outputPath=output_path)

    print(f"    ----> Completed processing (#{file_count}) -- {scan_file_path}")
    


