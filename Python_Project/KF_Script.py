import numpy

class KF:
    def __init__(self, initial_x:float, initial_v:float, accel_variance:float):
        #mean
        self._x = numpy.array([initial_x, initial_v])
        self._accel_variance=accel_variance
        #covariance
        self._P = numpy.eye(2)

    def predict(self, dt:float):
        #x=F*x
        #P=F*P*Ft*G*Gt*a
        F = numpy.array(([1,dt],[0,1]))
        F_transpose = numpy.transpose(F)
        G = numpy.array([0.5*dt**2,dt]).reshape((2,1))
        G_transpose = numpy.transpose(G)

        new_x = F.dot(self._x)  # Dot-Product from (F)(x)
        new_P=F.dot(self._P).dot(F_transpose) + G.dot(G_transpose)*self._accel_variance

        pass

    @property
    def pos(self):
        return self._x[0]

    @property
    def vel(self):
        return self._x[1]
