BOARD_TAG    = uno
AVRDUDE_CONF = /etc/avrdude.conf
ARDUINO_LIBS = Wire SoftwareSerial
include ${ARDMK_DIR}/Arduino.mk

PORT         = /dev/ttyUSB0
COM_SPEED    = 9600

deploy: clean
	make
	make upload serial

serial:
	miniterm.py $(PORT) $(COM_SPEED)

connect:
	# exit: ^a ^x
	picocom -b $(COM_SPEED) --omap crcrlf $(PORT)
