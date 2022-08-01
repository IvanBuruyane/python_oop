def get_loss(w1, w2, w3, w4):
    try:
        first_step = 10 * w1 // w2
    except:
        return "деление на ноль"
    else:
        return first_step - 5 * w2 * w3 + w4


