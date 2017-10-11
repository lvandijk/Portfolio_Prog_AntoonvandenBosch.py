cijfers = {'Antoon':9.0,'Huub':9.1,'Sebastiaan':10,'Bart':4,'Leon':9.4,'Wessel':7,'Ryne':6,'Hidde':5}

for key in cijfers:
    if cijfers.get(key) > 9.0:
        print('{}: {}'.format(key, float(cijfers.get(key))))