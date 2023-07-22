import random
import string
import multiprocessing
import csv 


def get_random_string(n=15):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


def get_random_numbers(n=8):
    start = 10**(n-1)
    end = (10**n)-1
    return random.randint(start, end)


def write_data_to_csv(filename, num_rows):
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(num_rows):
            writer.writerow([get_random_string(), get_random_numbers()])


if __name__ == "__main__":
    quantity = 100
    file = f'data_{quantity}.csv'
    write_data_to_csv(file, quantity)


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