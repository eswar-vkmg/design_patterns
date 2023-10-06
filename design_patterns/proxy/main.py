from proxy import LazyBookParser

if __name__ == '__main__':
    lazy_bp_1 = LazyBookParser()
    lazy_bp_2 = LazyBookParser

    print(lazy_bp_1.get_number_of_pages())
    print(lazy_bp_1.get_number_of_pages())

    # We can observe that even though lazy_bp_2 was created, the method was not called.
    # So by deferring the expensive obj creation, by proxying, we have saved against exp operation
