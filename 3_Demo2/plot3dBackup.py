import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# we are going to plot the 3d trajectory defined by the vicon data


def plot3d(data):
    matplotlib.use("TkAgg")
    print(data)
    x = data["data"]["x"]
    y = data["data"]["y"]
    z = data["data"]["z"]
    Rx = data["data"]["Rx"]
    Ry = data["data"]["Ry"]
    Rz = data["data"]["Rz"]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(x, y, z, c=z, cmap="viridis")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Trajectory")

    ax.set_box_aspect([1, 1, 1])
    plt.show()


def parse_data(data):
    x = data["TX"].to_numpy() / 1000
    y = data["TY"].to_numpy() / 1000
    z = data["TZ"].to_numpy() / 1000
    Rx = data["RX"].to_numpy()
    Ry = data["RY"].to_numpy()
    Rz = data["RZ"].to_numpy()
    return {"data": {"x": x, "y": y, "z": z, "Rx": Rx, "Ry": Ry, "Rz": Rz}}


def main():
    data = pd.read_csv("Demo2/Cleaned_Data.csv")  # run from main dir

    # ask the question "what does pd.read_csv data do"?
    # WHEN TO READ VS WHEN NOT TO READ...
    data = parse_data(data)

    plot3d(data)


if __name__ == "__main__":
    main()
