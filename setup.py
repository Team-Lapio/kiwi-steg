from setuptools import find_packages, setup

setup(name='kiwi-steg',
      version='0.5',
      description='Image Steganography Sandbox',
      url='https://github.com/Team-Lapio/kiwi-steg',
      author='Team Lapio',
      author_email='teamlapio@gmail.com',
      packages=find_packages(),
      install_requires=[
          'pyqt5',
          'pillow'
      ],
      python_requires='>=3',
      zip_safe=False)