# 블루투스 페어링이 먼저 되어 있어야한다.


# Add divice 클릭


# 페어링


# 블루투스를 통해 SPP service를 사용

# /etc/systemd/system/dbus-org.bluez.service 에 들어감

# 추가 해야 할 것

# ExecStart=/usr/lib/bluetooth/bluetoothd -C
# ExecStartPost=/usr/bin/sdptool add SP

# 추가 이후 저장하고 재부팅

# 설치 해야 할 파일
# sudo apt install libbluetooth-dev
# sudo apt install python-dev
# sudo pip3 install PyBluez

# 라즈베리파이가 서버, 스마트폰이 클라이언트



