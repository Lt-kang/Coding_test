def solution(k, b):
    arrows = {'left': [-1, 0],
              'right': [1, 0],
              'up': [0, 1],
              'down': [0, -1]}
    x = 0
    y = 0
    
    for a in k:
        x_ = arrows[a][0]
        y_ = arrows[a][1]
        
        if abs(x + x_) <= b[0]//2:
            x += x_
        if abs(y + y_) <= b[1]//2:
            y += y_
        
    return [x, y]