from multiprocessing import Process,current_process,Manager

def func(name:str,m_list:list,m_dict:dict):
    m_dict['name']='Jerry'
    m_list.append('hello')

if __name__=="__main__":
    with Manager() as mgr:
        m_list=mgr.list()
        m_dict=mgr.dict()
        m_list.append('泥嚎')

        p1=Process(target=func,args=('p1',m_list,m_dict))
        p1.start()
        p1.join()
        print(m_list)
        print(m_dict)