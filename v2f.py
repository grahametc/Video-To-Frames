import cv2 as cv
import os, sys, argparse

#frames must be in numerical order
def merge_frames(path, fps):
   os.chdir(path)
   data = cv.imread(os.listdir(path)[0])
   size = data.shape
   fourcc = cv.VideoWriter_fourcc(*'mp4v')
   output = cv.VideoWriter("output.mp4", fourcc, fps, (size[1], size[0]))   
   for i in range(1, len(os.listdir(path))):
      img = cv.imread(str(i)+".png")
      output.write(img)
   cv.destroyAllWindows()
   output.release

def get_frames(path):
   new_dir = path + "_frames" 
   cmd = "mkdir " + new_dir
   if not os.path.isdir(new_dir):
      os.system(cmd)
   else:
       for file in os.listdir(new_dir):
           os.remove(new_dir + "/" + file)
       os.rmdir(new_dir)
       os.system(cmd)
   vid = cv.VideoCapture(path)
   if not vid.isOpened():
         print("Cannot open video")
         sys.stderr
         exit()
   frame_count=0
   os.chdir(new_dir)
   while True:
       ret, frame = vid.read()
      
       if not ret:
           break
       
       frame_count+=1
       cv.imwrite(str(frame_count)+".png", frame)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Video to frames and vice versa.")
    parser.add_argument("-path", "-p", required=True, help="Path to directory or video.")
    parser.add_argument("-fps", "-fps", default=24, help = "Frame rate for video. (Default is 24)")
    parser.add_argument("-video", "-v", action=argparse.BooleanOptionalAction, help="Convert a video to frames.")
    parser.add_argument("-frames", "-f", action=argparse.BooleanOptionalAction, help="Convert frames to a video.")
    args = parser.parse_args()

    if(args.video and args.frames):
        print("Incorrect Usage.")
        exit()
    if(args.video): merge_frames(args.path, int(args.fps))
    elif(args.frames): get_frames(args.path)
    else: print("Incorrect usage.")
    