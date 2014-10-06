'''
Interfaces required for using the parameter estimation methods

@author: Jerker Nordh
'''
import abc

class ParamEstInterface(object):
    """ Interface s for particles to be used with the parameter estimation
        algorithm presented in [1]
        [1] - 'System identification of nonlinear state-space models' by 
              Schon, Wills and Ninness """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_params(self, params):
        """ New set of parameters for which the integral approximation terms will be evaluated"""
        pass

    @abc.abstractmethod
    def eval_logp_x0(self, particles, t):
        """ Calculate gradient of a term of the I1 integral approximation
            as specified in [1].
            The gradient is an array where each element is the derivative with 
            respect to the corresponding parameter"""
        pass

    def eval_logp_xnext(self, particles, particles_next, u, t):
        """ Calculate gradient of a term of the I2 integral approximation
            as specified in [1].
            The gradient is an array where each element is the derivative with 
            respect to the corresponding parameter"""
        # Here we can just reuse the method used in the particle smoothing as default
        return self.logp_xnext(particles, particles_next, u, t)

    def eval_logp_y(self, particles, y, t):
        """ Calculate gradient of a term of the I3 integral approximation
            as specified in [1].
            The gradient is an array where each element is the derivative with 
            respect to the corresponding parameter"""

        # Default implementation, doesn't work for classes were the measure updates
        # the internal state of the particle (e.g Rao-Blackwellized models)
        return self.measure(particles, y, t)



class ParamEstInterface_GradientSearch(ParamEstInterface):
    """ Interface s for particles to be used with the parameter estimation
        algorithm presented in [1]
        [1] - 'System identification of nonlinear state-space models' by 
              Schon, Wills and Ninness """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def eval_logp_x0_val_grad(self, particles):
        """ Calculate gradient of a term of the I1 integral approximation
            as specified in [1].
            The gradient is an array where each element is the derivative with 
            respect to the corresponding parameter"""
        pass

    @abc.abstractmethod
    def eval_logp_xnext_val_grad(self, particles, particles_next, u, t):
        """ Calculate gradient of a term of the I2 integral approximation
            as specified in [1].
            The gradient is an array where each element is the derivative with 
            respect to the corresponding parameter"""
        pass

    @abc.abstractmethod
    def eval_logp_y_val_grad(self, particles, y, t):
        """ Calculate gradient of a term of the I3 integral approximation
            as specified in [1].
            The gradient is an array where each element is the derivative with 
            respect to the corresponding parameter"""
        pass
