import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from pypcd import pypcd


def invert_tf_matrix(tf_matrix):
    # Aufgabe 1.1:
    #     Invertiere die gegebene 4x4-Transformationsmatrix wie in der Vorlesung hergeleitet
    #
    #     Hinweis: Bequeme Matrixmultiplikation mit Numpy: produkt = a @ b

    # ------------------ Dein Code Hier ------------------ #


    return np.eye(4)


def load_data(pcl_path, img_path):
    pcd = pypcd.PointCloud.from_path(pcl_path)
    pc_data = pcd.pc_data
    scan = np.array([pc_data["x"], pc_data["y"], pc_data["z"], pc_data["intensity"]], dtype=np.float32)
    points = scan[0:3, :].T
    intensities = np.sqrt(scan[0, :] ** 2 + scan[1, :] ** 2 + scan[2, :] ** 2)
    img = mpimg.imread(img_path)
    return (points, intensities), img


def apply_homogeneous_transformation(tf, points_3d):
    points_4d = np.insert(points_3d, 3, 1, axis=1)
    points_transformed = points_4d @ tf.T
    return points_transformed[:, :3]


def project(points_3d, fx, fy, cx, cy):
    projection_matrix = np.array([[fx, 0.0, cx], [0.0, fy, cy], [0.0, 0.0, 1.0]])
    points_2d_hom = points_3d.dot(projection_matrix.T)
    points_2d_hom = points_2d_hom / points_2d_hom[:, 2].reshape(-1, 1)
    return points_2d_hom[:, :2]


def plot_projection(img, points_2d, intensities, window_title="Figure"):
    plt.figure(figsize=(12, 5), dpi=96, tight_layout=True)
    plt.axis([0, img.shape[1], img.shape[0], 0])
    plt.imshow(img, 'Greys_r')
    plt.scatter(points_2d[:, 0], points_2d[:, 1], c=[intensities], cmap='plasma_r', alpha=1.0, s=2)
    plt.axis('off')
    man = plt.get_current_fig_manager()
    man.set_window_title(window_title)
    plt.show()
