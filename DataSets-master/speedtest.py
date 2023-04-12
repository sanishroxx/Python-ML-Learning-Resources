import speedtest
st = speedtest.Speedtest()
option = int(input('''what speed do you want to test:
1) Download Speed
2) Upload Speed
3) Ping
Your Choise: '''))

if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("please enter the correct choise !")