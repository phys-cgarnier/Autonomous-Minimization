import devsup.ptable as pt


class ParamTable(pt.TableBase):
    def set_param(self,param,value):
        attr = getattr(self,param)
        attr.value = value
        attr.notify()
        return True