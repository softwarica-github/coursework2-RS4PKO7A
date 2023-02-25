import unittest
from tkinter import *
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os
from image_steganography_second import *

class StegnoTest(unittest.TestCase):

    def setUp(self):
        self.stegno = Stegno()

    def test_decode(self):
        # Test case for decode method
        image = Image.open("test_image.png", 'r')
        expected_output = "Hello, this is a test message for decoding."
        decoded_data = self.stegno.decode(image)
        self.assertEqual(decoded_data, expected_output)

    def test_main(self):
        # Test case for main method
        root = Tk()
        self.stegno.main(root)
        title_label = root.grid_slaves(row=0, column=0)[0]
        self.assertEqual(title_label.cget("text"), "SimpleSteganography")

    def test_home(self):
        # Test case for home method
        root = Tk()
        self.stegno.main(root)
        encode_button = root.grid_slaves(row=2, column=0)[0]
        encode_button.invoke()
        self.stegno.home(root)
        title_label = root.grid_slaves(row=0, column=0)[0]
        self.assertEqual(title_label.cget("text"), "SimpleSteganography")

    def test_frame1_decode(self):
        # Test case for frame1_decode method
        root = Tk()
        self.stegno.frame1_decode(root)
        label_art = root.grid_slaves(row=1, column=0)[0]
        self.assertEqual(label_art.cget("text"), "Please")

    def test_frame2_decode(self):
        # Test case for frame2_decode method
        root = Tk()
        self.stegno.frame2_decode(root)
        label_art = root.grid_slaves(row=1, column=0)[0]
        self.assertEqual(label_art.cget("text"), "Select Image with Hidden text:")

    def test_frame1_encode(self):
        # Test case for frame1_encode method
        root = Tk()
        self.stegno.frame1_encode(root)
        label_art = root.grid_slaves(row=1, column=0)[0]
        self.assertEqual(label_art.cget("text"), "Please")

    def test_frame2_encode(self):
        # Test case for frame2_encode method
        root = Tk()
        self.stegno.frame2_encode(root)
        label_art = root.grid_slaves(row=1, column=0)[0]
        self.assertEqual(label_art.cget("text"), "Select the Image in which \nyou want to hide text :")
if __name__ == '__main__':
    unittest.main()

