import controller as c
import logging as log

# # Если хотим, чтобы логи выводились в консоль
# log.basicConfig(level=log.INFO)

# Если хотим, чтобы логи записывались в файл
log.basicConfig(filename='Seminar07_calc\log.txt',
                filemode='a',
                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                datefmt='%H:%M:%S',
                level=log.INFO)


c.run(log)
