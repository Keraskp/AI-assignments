import string
import random
import threading
import multiprocessing
import time


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_numbers(length):
    numbers = '0123456789'
    result_num = ''.join(random.choice(numbers) for i in range(length))
    if result_num[0] == '0':
        result_num = random.choice(numbers[1:]) + result_num[1:]
    return int(result_num)


def get_data(file, gen_num_fills):
    for _ in range(gen_num_fills):
        file.write(f'{get_random_string(15)},{get_random_numbers(10)}\n')
        file.flush()


def multi_process(file, gen_nums, num_process=250):
    num_processes = num_process
    gen_num_fill = gen_nums//num_processes
    processes = [multiprocessing.Process(target=get_data, args=(
        file, gen_num_fill)) for _ in range(num_processes)]
    for process in processes:
        process.start()

    for process in processes:
        process.join()


def single_process(file, gen_nums):
    for _ in range(gen_nums):
        get_data(file, 1)


def create_data(quantity):
    file = open(f'data_{quantity}.csv', 'w')
    if quantity < 50_000:
        single_process(file, quantity)
    else:
        multi_process(file, quantity)
    file.close()


if __name__ == '__main__':
    # gen_nums = 1_000_000
    # file = open(f'data_{gen_nums}.csv', 'w')

    # # Not processing
    # start = time.perf_counter()
    # single_process(file, gen_nums)
    # end = time.perf_counter()
    # print(end - start)

    # # Threading
    # start = time.perf_counter()
    # multi_process(file, gen_nums)
    # end = time.perf_counter()
    # print(end - start)

    # file.close()

    create_data(1000)
