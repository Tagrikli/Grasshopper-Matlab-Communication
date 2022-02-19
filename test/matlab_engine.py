import matlab.engine

engine = matlab.engine.start_matlab()
result = engine.isprime(37)
print(result)
engine.quit()
