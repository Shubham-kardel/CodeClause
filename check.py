import pyshorteners



def short(url):
    st = pyshorteners.Shortener()
    s = st.tinyurl.short(url)
    return s
    # print("The shortend url is : ",s)

