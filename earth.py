import time

def get_frames():
    frames = dict()
    for num in range(1, 14):
        with open(f'earth/planet_{num}.md', 'r') as file:
            frames[num] = file.read()
    return frames


def run_earth():
    frames = get_frames()
    step = 1
    print('\u001b[32m')
    while True:
        print(frames[step], end='')
        time.sleep(0.5)
        print('\u001b[23A', end='')
        if step == len(frames):
            step = 1
        else:
            step += 1

if __name__ == '__main__':
    run_earth()
    