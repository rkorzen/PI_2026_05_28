import logging

logging.basicConfig(
    filename="logs.log",
    level=logging.ERROR,
)
logger = logging.getLogger()

x=1
y=0
try:
    x/y
except:
    logger.error(f"Cos nie tak z danymi, x={x}, y={y}")

print("Dalej..")


# lepiej


x=1
y=0
try:
    #x/y
    x/"A"
except ZeroDivisionError:
    logger.error(f"y jest 0. To nie powinno miec miejsca. Sprawdz to!")
except TypeError:
    logger.error(f"Cos nie tak z danymi x ={x}, y={y}")

print("Dalej..")