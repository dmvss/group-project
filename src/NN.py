import keras

def NN_load_model(path):
    NN_model = keras.models.load_model(path)
    return NN_model

def NN_predict(model, data):
    return model.predict(data, verbose=0)

def NN_classify(prediction):
    return prediction[0] < prediction[1]

def NN_get_label(value):
    if value == 0:
        return "NON VPN"
    else:
        return "VPN"

def NN_classify_batch(prediction_batch):

    non_vpn = 0
    vpn = 0
    total = len(prediction_batch)

    for prediction in prediction_batch:
        ret = NN_classify(prediction)
        if ret == 0:
            non_vpn += 1
        else:
            vpn += 1

    label = ''
    confidence = 0

    if vpn > non_vpn:
        label = 'VPN'
        confidence = round((vpn / total), 2)
    else:
        if vpn < non_vpn:
            label = 'NON VPN'
            confidence = round((non_vpn / total), 2)
        else:
            label = '50/50'
            confidence = 1
    
    return label, confidence

def NN_classify_batch_debug(prediction_batch):
    
    debug = []

    for prediction in prediction_batch:

        non_vpn = round(prediction[0], 2)
        vpn = round(prediction[1], 2)

        ret = NN_classify(prediction)
        label = NN_get_label(ret)

        debug.append((str(non_vpn), str(vpn), label))
    
    return debug