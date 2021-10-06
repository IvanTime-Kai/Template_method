from HomeTemplate import HomeTemplate
from PageTemplate import PageTemplate
from DetailTemplate import DetailTemplate
from ContactTemplate import ContactTemplate

def clent_call(pageTemplate: PageTemplate):
    pageTemplate.Template_Method();



if __name__ == '__main__':
    print('Home page')
    clent_call(HomeTemplate())
    print('--------------------------------------')
    print('Detail page')
    clent_call(DetailTemplate())
    print('--------------------------------------')
    print('Contact page')
    clent_call(ContactTemplate())

