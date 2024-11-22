import os, serial, time, csv

ser = serial.Serial("/dev/tty.usbserial-14220", 115200, timeout=1)
gestures = ["pause", "play", "resume", "back", "skip"]

for gesture in gestures:
    for trial in range(21):
        # set filename
        filename = f"{gesture}_{trial:02d}.csv"

        # countdown to capture data
        print(f"starting collecting data for {gesture} gesture, and {trial} trial")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        print("start")

        # now we have to write to open connection, write to csv
        # we should first setup the file to have the specified rows and columns
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["acce_x", "acce_y", "acce_z", "gyro_x", "gyro_y", "gyro_z"]
            )

            curTime = time.time()
            while time.time() - curTime < 4:
                # this should read in data from the ser and write it to the file
                line = ser.readline().decode("utf-8").strip()
                if line:
                    data = line.split(",")
                    if len(data) == 6:
                        writer.writerow(data)
        print(f"Saved {filename}")
ser.close()
