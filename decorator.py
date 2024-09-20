import inspect


def no_none_allowed(f):

    def wrapper(*args, **vargs):
        values = args + tuple(vargs.values())
        if any(parm is None for parm in values):
            keys = f.__code__.co_varnames[:f.__code__.co_argcount]
            print(keys)
            print(values)
            res = dict(zip(keys, values))
            print("Resultant dictionary is : " + str(res))
            is_none = list(filter(lambda k: res[k] is None, res))
            print("None values : " + str(is_none))
            return None
        return f(*args, **vargs)
    return wrapper


class Testing(object):

    @no_none_allowed
    def add_transaction(self, name, date, amount, debit, user, category_id):
        print(name, date, amount, debit, user, category_id)


Testing.add_transaction(1, None, 3, None, 5, user=12, category_id=66)
Testing.add_transaction(1, 10, 3, 1, 5, user=12, category_id=66)
