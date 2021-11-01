def features(data):
    """
    compute features for a single signature
    :param data: datas for a signature
    :return: x: vector containing features vectors
    """
    x = []
    vx, vy, dt = 0, 0, 0.01
    for i in range(len(data)):
        feature_vector = []
        if i != 0:
            vx = (data[1][i] - data[1][i - 1]) / dt
            vy = (data[2][i] - data[2][i - 1]) / dt

        feature_vector.append(data[1][i])   # x
        feature_vector.append(data[2][i])   # y
        feature_vector.append(vx)           # vx
        feature_vector.append(vy)           # vy
        feature_vector.append(data[3][i])   # pressure

        x.append(feature_vector)

    return x
