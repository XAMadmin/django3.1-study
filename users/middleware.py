def my_middleware(get_response):
    # 在Django第一次配置和初始化的时候执行一次
    print('init 被调用')

    def middleware(request):
        # 在每个请求处理视图前被调用。
        print('before request 被调用')

        response = get_response(request)

        # 在每个请求处理视图之后被调用。
        print('after response 被调用')
        return response

    return middleware