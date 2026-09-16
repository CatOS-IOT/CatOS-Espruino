# ==============================================================================
# 本文件由 catos espruino generate 根据 config/build.json 自动生成 —— 请勿手动修改。
# 构建配置的唯一真相源是 config/build.json;改完运行 catos espruino generate 重新生成。
# ==============================================================================
#!/bin/false

import copy

import ESP32S3_IDF5 as _base

info = copy.deepcopy(_base.info)
chip = copy.deepcopy(_base.chip)
devices = copy.deepcopy(_base.devices)
boards = copy.deepcopy(_base.boards)
get_pins = _base.get_pins

info.update({
    'name': 'ESP32S3',
    'espruino_page_link': 'ESP32',
    'default_console': 'EV_SERIAL1',
    'default_console_baudrate': '115200',
    'variables': 4095,
    'io_buffer_size': 4096,
    'binary_name': 'espruino_%v_esp32s3.bin',
})

info['build'].update({
    'optimizeflags': '-Og',
    'libraries': ['ESP32', 'NET', 'GRAPHICS', 'CRYPTO', 'SHA256', 'SHA512', 'TLS', 'TELNET', 'NEOPIXEL', 'FILESYSTEM', 'BLUETOOTH'],
    'makefile': ['DEFINES+=-DESP_PLATFORM -DESP32=1', 'DEFINES+=-DESP_STACK_SIZE=25000', 'DEFINES+=-DJSVAR_MALLOC', 'DEFINES+=-DUSE_FONT_6X8', 'DEFINES+=-DESPR_USE_USB_SERIAL_JTAG -DUSB', 'ESP32_FLASH_MAX=1572864'],
})

chip.update({
    'part': 'ESP32S3',
    'family': 'ESP32_IDF5',
    'ram': 512,
    'speed': 240,
    'usart': 3,
    'spi': 2,
    'i2c': 2,
    'adc': 2,
    'saved_code': {'address': 0x320000, 'page_size': 4096, 'pages': 224, 'flash_available': 1344},
})

info['boardname'] = 'ESP32S3_CATOS'
