import pickle, os


class cache():
    PATH = os.path.split(os.path.realpath(__file__))[0] + '/cache/'

    def save(self, key, value):
        f = open(self.PATH + key + ".cache", 'wb')
        pickle.dump(value, f, 2)
        f.close()

        return True
        pass

    def get(self, key):
        try:
            fr = open(self.PATH + key + ".cache", 'rb')
            return pickle.load(fr)
            pass

        except:

            return False

        pass
