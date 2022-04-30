# Environment for Raspberry Pi OS

## 1. Clash

1. Download clash from GitHub https://github.com/Dreamacro/clash/releases for Cortex A7

   ```shell
   wget https://github.com/Dreamacro/clash/releases/download/v1.10.0/clash-linux-armv7-v1.10.0.gz
   ```

2. Unzip the file and make it executable

   ```shell
   gunzip clash-linux-armv7-v1.10.0.gz
   sudo chmod 777 clash-linux-armv7-v1.10.0.gz
   ```

3. Move it to `/usr/bin/` so that we can just type clash rather than the full path to the file

   ```
   sudo mv clash-linux-armv7-v1.10.0.gz /usr/bin/clash
   ```

4. Configure the clash: I simply copy the configure files from my macOS. Two files need to add `config.yaml` and `Country.mmdb`

   ```sh
   mkdir ~/.config/clash
   mv config.yaml Country.mmdb ~/.config/clash
   ```

5. Enable proxy: add following lines to the end of the file `/etc/environment`. You can open it by typing `sudo vim /etc/environment`

   ```shell
   export http_proxy="http://127.0.0.1:7890"
   export https_proxy="http://127.0.0.1:7890"
   export no_proxy="localhost, 127.0.0.1"
   ```

6. Enable proxy for sudo operation

   ```sh
   sudo visudo
   ```

   Add the following line to the file:

   ```shell
   Defaults    env_keep+="http_proxy https_proxy no_proxy"
   ```

7. Run clash!

   ```shell
   clash &
   ```

## 2. Open CV

1. Run following scripts. You can paste them into a bash shell file, for example `install_opencv_depends.sh` and then type `bash install_opencv_depends.sh `

   ```sh
   sudo apt update
   sudo apt upgrade
   sudo apt install -y build-essential cmake pkg-config
   sudo apt install -y libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
   sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
   sudo apt install -y libxvidcore-dev libx264-dev
   sudo apt install -y libfontconfig1-dev libcairo2-dev
   sudo apt install -y libgdk-pixbuf2.0-dev libpango1.0-dev
   sudo apt install -y libgtk2.0-dev libgtk-3-dev
   sudo apt install -y libatlas-base-dev gfortran
   sudo apt install -y libhdf5-dev libhdf5-serial-dev libhdf5-103
   sudo apt install -y libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5
   ```

2. Install opencv from `pip`

   ```shell
   pip install opencv-python
   ```

   
