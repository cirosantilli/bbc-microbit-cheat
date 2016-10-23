# Getting started

## Local install

No proprietary web editors for me, thanks.

Ubuntu 16.04:

    # arm-none-eabi- 5.X...
    sudo add-apt-repository -y ppa:team-gcc-arm-embedded
    sudo apt-get remove binutils-arm-none-eabi gcc-arm-none-eabi
    sudo apt-get install gcc-arm-embedd

    # pip3 does not give the executable for some reason?
    sudo pip install yotta
    git clone https://github.com/bbcmicrobit/micropython
    git checkout 525d88c73f2b81d319efa3889cf5424ebfdc1770
    yotta target bbc-microbit-classic-gcc-nosd
    yotta up
    yotta build

TODO fails with: <https://github.com/bbcmicrobit/micropython/issues/338> Apparently only tested on GCC 6.X...

## Local emulators

TODO. Do any open ones exist? Hopefully compiled.
