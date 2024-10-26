#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking (UCAN) Lab, University of Massachusetts, Boston.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class OWC_Channel_relative_python(gr.sync_block):
    """
    docstring for block OWC_Channel_relative_python
    """
    def __init__(self, num_inputs = 1, num_outputs = 1, emission_angle_array = [1.0], acceptance_angle_array = [1.0], distance_array = [1.0], lambertian_order_array = [1.0], photosensor_area_array = [1.0], optical_filter_transmittance_array = [1.0], refractive_index_array =  [1.0], concentrator_FOV_array =  [90], E2O_conversion_factor_array = [1.0] ,O2E_conversion_factor_array = [1.0]):
        gr.sync_block.__init__(self,
            name="OWC_Channel_relative_python",
            in_sig=[np.float32] * num_inputs,
            out_sig=[np.float32] * num_outputs)
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.emission_angle_array = emission_angle_array
        self.acceptance_angle_array = acceptance_angle_array
        self.distance_array = distance_array
        self.lambertian_order_array = lambertian_order_array
        self.photosensor_area_array = photosensor_area_array
        self.optical_filter_transmittance_array = optical_filter_transmittance_array
        self.refractive_index_array = refractive_index_array
        self.E2O_conversion_factor_array = E2O_conversion_factor_array
        self.O2E_conversion_factor_array = O2E_conversion_factor_array
        self.concentrator_FOV_array = concentrator_FOV_array
        self.channel_model_values = []
        self.set = True

        self.calculate_channel_model_values()

    def calculate_channel_model_values(self):
        self.channel_model_values = []
        nout = self.get_num_outputs();
        nin = self.get_num_inputs();
        for x in range(nout):
            for j in range(nin):
                Gt = 0
                Gr = 0
                H = 0
                
                index = x * nin + j
                emission_angle = self.get_emission_angle_array()[index]
                acceptance_angle = self.get_acceptance_angle_array()[index]
                distance = self.get_distance_array()[index]
                lambertian_order = self.get_lambertian_order_array()[j]
                photosensor_area = self.get_photosensor_area_array()[x]
                optical_filter_transmittance = self.get_optical_filter_transmittance_array()[x]
                refractive_index = self.get_refractive_index_array()[x]
                concentrator_FOV = self.get_concentrator_FOV_array()[x]
                E2O_conversion_factor = self.get_E2O_conversion_factor_array()[j]
                O2E_conversion_factor = self.get_O2E_conversion_factor_array()[x]
                
                Gt = (lambertian_order + 1) / (2 * np.pi) * np.power(np.cos(np.radians(emission_angle)), lambertian_order) if emission_angle <= 90 else 0
                Gr = photosensor_area * optical_filter_transmittance * (refractive_index ** 2 / np.sin(np.radians(concentrator_FOV)) ** 2) * np.cos(np.radians(acceptance_angle)) if abs(acceptance_angle) <= concentrator_FOV else 0
                H = E2O_conversion_factor * (Gt * Gr / (distance ** 2)) * O2E_conversion_factor
                
                self.channel_model_values.append(H)
        self.set = False


    def work(self, input_items, output_items):
        ninputs = len(input_items)
        noutputs = len(output_items)

        if self.set:
            self.calculate_channel_model_values()

        for i in range(len(output_items[0])):
            for x in range(noutputs):
                received_power = 0.0

                for j in range(ninputs):
                    index = x * ninputs + j 
                    received_power += input_items[j][i] * self.channel_model_values[index]

                output_items[x][i] = received_power
                
        return len(output_items[0])
            
    def set_num_inputs(self, num_inputs):
        self.num_inputs = num_inputs
        self.set = True 

    def get_num_inputs(self):
        return self.num_inputs

    def set_num_outputs(self, num_outputs):
        self.num_outputs = num_outputs
        self.set = True 

    def get_num_outputs(self):
        return self.num_outputs

    def set_emission_angle_array(self, emission_angle_array):
        self.emission_angle_array = emission_angle_array
        self.set = True 

    def get_emission_angle_array(self):
        return self.emission_angle_array
       
    def set_acceptance_angle_array(self, acceptance_angle_array):
        self.acceptance_angle_array = acceptance_angle_array
        self.set = True 
           
    def get_acceptance_angle_array(self):
        return self.acceptance_angle_array
      
    def set_distance_array(self, distance_array):
        self.distance_array = distance_array
        self.set = True 
       
    def get_distance_array(self):
        return self.distance_array
   
    def set_lambertian_order_array(self, lambertian_order_array):
        self.lambertian_order_array = lambertian_order_array
        self.set = True 
   
    def get_lambertian_order_array(self):
        return self.lambertian_order_array

    def set_photosensor_area_array(self, photosensor_area_array):
        self.photosensor_area_array = photosensor_area_array
        self.set = True 
   
    def get_photosensor_area_array(self):
        return self.photosensor_area_array

    def set_optical_filter_transmittance_array(self, optical_filter_transmittance_array):
        self.optical_filter_transmittance_array = optical_filter_transmittance_array
        self.set = True 
   
    def get_optical_filter_transmittance_array(self):
        return self.optical_filter_transmittance_array

    def set_refractive_index_array(self, refractive_index_array):
        self.refractive_index_array = refractive_index_array
        self.set = True 
   
    def get_refractive_index_array(self):
        return self.refractive_index_array

    def set_concentrator_FOV_array(self, concentrator_FOV_array):
        self.concentrator_FOV_array = concentrator_FOV_array
        self.set = True 
   
    def get_concentrator_FOV_array(self):
        return self.concentrator_FOV_array

    def set_E2O_conversion_factor_array(self, E2O_conversion_factor_array):
        self.E2O_conversion_factor_array = E2O_conversion_factor_array
        self.set = True 
   
    def get_E2O_conversion_factor_array(self):
        return self.E2O_conversion_factor_array

    def set_O2E_conversion_factor_array(self, O2E_conversion_factor_array):
        self.O2E_conversion_factor_array = O2E_conversion_factor_array
        self.set = True 
   
    def get_O2E_conversion_factor_array(self):
        return self.O2E_conversion_factor_array
