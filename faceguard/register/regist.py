import os
from tqdm import tqdm
from .register import register
current_path = os.path.dirname(__file__)
parent_path = os.path.dirname(current_path)
pkl_path_ = 'F:\\NUS\\Group Project\\Pattern Recognition\\login\\FaceGuard\\data\\'
def user_reg(img):
# if __name__ == '__main__':
    resume = current_path + './lib/070.ckpt'
    pkl_path = pkl_path_ + './db_features.pkl'
    gallery_path = parent_path+'./cropped_gallery/'
    #imgs = os.listdir(gallery_path)
    # for img in tqdm(imgs):
    img_path = gallery_path + img
    r = register(resume, gpu=False)
    r.run(pkl_path, img_path)
    print("registration succesully")