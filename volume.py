            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #~                                                                         ~#
            #~                                --Volume--                               ~#    
            #~                                                                         ~#   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~                                                                                                ~#
#~   --Algorithm--                                                                                ~#  
#~                                                                                                ~#
#~   design `Volume` class to embody methods programmed with only local variables                 ~#
#~   design the following methods:                                                                ~#
#~      1   __init__(self, magnitude, units)                                                      ~#                           
#~      2   __str__(self)                                                                         ~#                   
#~      3   __repr__(self)                                                                        ~#                   
#~      4   is_valid(self)                                                                        ~#                    
#~      5   get_units(self)                                                                       ~#                     
#~      6   get_magnitude(self)                                                                   ~#                         
#~      7   metric(self)                                                                          ~#                  
#~      8   customary(self)                                                                       ~#                     
#~      9   __eq__(self, other)                                                                   ~#                         
#~      10  add(self, other)                                                                      ~#
#~      11  sub(self, other)                                                                      ~#   
#~                                                                                                ~#              
#~      These main methods are assisted by the following `helper` methods:                        ~#     
#~      1   make_metric(self)                                                                     ~#
#~      2   make_customary(self)                                                                  ~#
#~      3   is_metric(self)                                                                       ~#          
#~      4   is_customary(self)                                                                    ~#   
#~      5   magnitude_is_valid(self)                                                              ~#                               
#~      6   units_is_valid(self)                                                                  ~#
#~      7   __validate__(self)                                                                    ~#  
#~      8   is_valid_contant(self, c)                                                             ~#  
#~                                                                                                ~#  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#===================================================================================================


class Volume:

    def __init__(self, magnitude=0, units="ml"):
        """ Construct `Volume` object with default volume magnitude & units set to `0` (int) & `ml` (str) respectively.
        """
        self.magnitude = magnitude
        self.units = units

        if not self.magnitude_is_valid():
            self.magnitude = 0
            self.units = None

        elif not self.units_is_valid():
            self.magnitude = None
            self.units = None

    def __str__(self):
        """ Returns the `magnitude` (str) formatted as a 3-decimal-place float separated from the `units` by a space.
        """
        if not self.__validate__():
            return "Not a Volume"
        else:
            return f"{self.magnitude:.3f} {self.units}"

    def __repr__(self):
        """ Returns the `magnitude` (str) formatted as a 6-decimal-place float separated from the `units` by a space.
        """
        if not self.__validate__():
            return "Not a Volume"
        else:
            return f"{self.magnitude:.6f} {self.units}"

    def is_valid(self):
        """ Returns `True` if `Volume` has positive `magnitude` & `units` of either `ml` or `oz` of type (str).
        """
        if self.__validate__():
            return 'V is valid'
        else:
            return False

    def get_units(self):
        """ Returns the `units` of the `Volume` object, stored during construction.
        """
        return self.units

    def get_magnitude(self):
        """ Returns the `magnitude` of the `Volume` object, stored during construction.
        """
        return self.magnitude

    def metric(self):    
        """ Returns a `Volume` object with metric system equivalents of volume magnitude and units.
        """

        if self.__validate__():
            metric_magnitude, metric_units = self.make_metric()
            return Volume(metric_magnitude, metric_units)
        else:
            return self

    def customary(self):
        """ Returns a `Volume` object with customary system equivalents of `Volume` magnitude and units. 
        """
        if self.__validate__():
            customary_magnitude, customary_units = self.make_customary()
            return Volume(customary_magnitude, customary_units)

        else:
            return self

    def __eq__(self, other):
        """ Evaluates the equality of two `Volume` instances.
        """
        DELTA = 0.000001

        if type(other) == Volume:

            if self.__validate__() and other.__validate__():

                if self.units == other.units:
                    diff = self.magnitude - other.magnitude
                    
                else:
                    if self.is_metric():
                        diff = self.magnitude - other.metric().magnitude
                        
                    elif self.is_customary():
                        diff = self.magnitude - other.customary().magnitude

                bool = abs(diff) < DELTA
                        
                return bool
        else:
            return False
        
    def add(self, other):
        """ Returns the sum of two valid `Volume` instances.
        """

        if type(other) == Volume:

            if self.__validate__() and other.__validate__():

                if self.units == other.units:
                    sum_magnitude = self.magnitude + other.magnitude 
                    
                else:
                    if self.is_metric():
                        sum_magnitude = self.magnitude + other.metric().magnitude
                        
                    elif self.is_customary():
                        sum_magnitude = self.magnitude + other.customary().magnitude
                        
                return Volume(sum_magnitude, self.units)
        
        elif self.is_valid_constant(other):
            
            sum_magnitude = self.magnitude + other
            return Volume(sum_magnitude, self.units)
            

        
    def sub(self, other):
        """ Returns the difference between two valid `Volume` instances.
        """
        if type(other) == Volume:

            if self.__validate__() and other.__validate__():

                if self.units == other.units:
                    diff_magnitude = self.magnitude - other.magnitude
                    
                else:
                    if self.is_metric():
                        diff_magnitude = self.magnitude - other.metric().magnitude
                        
                    elif self.is_customary():
                        diff_magnitude = self.magnitude - other.customary().magnitude

                return Volume(diff_magnitude, self.units)

        elif self.is_valid_constant(other):

            sum_magnitude = self.magnitude - other
            return Volume(sum_magnitude, self.units)
                
    # --------------------------------------------- HELPER METHODS ----------------------------------------------
    def make_metric(self):
        """ Returns the equivalent metric system `magnitude` & `units` for an already VALID `Volume` object.
        """
        ML_PER_1FLOZ = 29.5735295625
        
        if self.is_metric():
            metric_magnitude = self.magnitude
        else:
            metric_magnitude = self.magnitude * ML_PER_1FLOZ

        metric_units = "ml"

        return metric_magnitude, metric_units

    def make_customary(self):
        """ Returns the equivalent customary system `magnitude` & `units` for an already VALID `Volume` object.
        """
        FLOZ_PER_1ML = 1/29.5735295625
        
        if self.is_customary():
            customary_magnitude = self.magnitude
        else: 
            customary_magnitude = self.magnitude * FLOZ_PER_1ML

        customary_units = "oz"

        return customary_magnitude, customary_units

    def is_metric(self):
        """ Returns `True` if the current `units` attribute of the `Volume` object is the string, `ml`.
        """
        if self.units == "ml":
            return True
        else:
            return False

    def is_customary(self):
        """ Returns `True` if the current `units` attribute of the `Volume` object is the string, `oz`.
        """
        if self.units == "oz":
            return True
        else:
            return False
    
    def magnitude_is_valid(self):
        """ Returns `True` IF `magnitude` attribute of the `Volume` object is a positve integer. i.e. `0` or greater. 
        """
        try:
            checker = float(self.magnitude)
            if checker >= 0:
                return True
            else:
                return False
        except:
            return False

    def units_is_valid(self):
        """ Returns `True` IF the `units` attribute of the `Volume` object has a string value of either `ml` or `oz`. 
        """
        VALID_UNITS = {"ml", "oz"}

        if self.units in VALID_UNITS:
            return True
        else:
            return False

    def __validate__(self):
        """ Returns `True` IF the `Volume` object has both positive `magnitude` & `units` of either `ml` or `oz` of type (str).
        """
        if self.magnitude_is_valid() and self.units_is_valid():
            return True
        else:
            return False

    def is_valid_constant(self, c):
        """ Returns `True` is a constant is a valid numeric value.
        """
        try:
            c = float(c)
            return True
        except:
            return False