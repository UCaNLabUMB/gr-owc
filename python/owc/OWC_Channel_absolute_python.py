#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Kunal Sangurmath from The Ubiquitous Communications and Networking(UCAN) Lab, University of Massachusetts, Boston.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class OWC_Channel_absolute_python(gr.sync_block):
    """
    docstring for block OWC_Channel_absolute_python
    """
    def __init__(self, num_inputs=1,num_outputs=1,tx_coordinates_array=[1.0,2.0,5.0],tx_orientation_array=[0.0,0.0,-1.0],rx_coordinates_array=[2.0,2.0,0.0],rx_orientation_array=[0.0,0.0,1.0],tx_lambertian_order_array=[2.0],rx_photosensor_area_array=[1.0],optical_filter_transmittance_array=[1.0],refractive_index_array=[1.0], clip_neg = True, shot_noise = False, sample_rate = 10000.0, responsivity = 1.0, concentrator_FOV_array=[90],E2O_conversion_factor_array=[1.0],O2E_conversion_factor_array=[1.0]):
        gr.sync_block.__init__(self,
            name="OWC_Channel_absolute_python",
            in_sig=[np.float32] * num_inputs,
            out_sig=[np.float32] * num_outputs)
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        self.tx_coordinates_array = tx_coordinates_array
        self.rx_coordinates_array = rx_coordinates_array
        self.tx_orientation_array = tx_orientation_array
        self.rx_orientation_array = rx_orientation_array
        self.tx_lambertian_order_array = tx_lambertian_order_array
        self.rx_photosensor_area_array = rx_photosensor_area_array
        self.optical_filter_transmittance_array = optical_filter_transmittance_array
        self.refractive_index_array = refractive_index_array
        self.clip_neg = clip_neg
        self.shot_noise = shot_noise
        self.sample_rate = sample_rate
        self.responsivity = responsivity
        self.concentrator_FOV_array = concentrator_FOV_array
        self.E2O_conversion_factor_array = E2O_conversion_factor_array
        self.O2E_conversion_factor_array = O2E_conversion_factor_array

        self.distance_array = []
        self.emission_angle_array = []
        self.acceptance_angle_array = []
        self.channel_model_values = []
        self.set = True

        self.set_distance_array()
        self.set_emission_angle_array()
        self.set_acceptance_angle_array()
        self.calculate_channel_model_values()
        
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

    def set_tx_coordinates_array(self, tx_coordinates_array):
        self.tx_coordinates_array = tx_coordinates_array
        self.set = True

    def get_tx_coordinates_array(self):
        return self.tx_coordinates_array

    def set_tx_orientation_array(self, tx_orientation_array):
        self.tx_orientation_array = tx_orientation_array
        self.set = True

    def get_tx_orientation_array(self):
        return self.tx_orientation_array

    def set_rx_coordinates_array(self, rx_coordinates_array):
        self.rx_coordinates_array = rx_coordinates_array
        self.set = True

    def get_rx_coordinates_array(self):
        return self.rx_coordinates_array

    def set_rx_orientation_array(self, rx_orientation_array):
        self.rx_orientation_array = rx_orientation_array
        self.set = True

    def get_rx_orientation_array(self):
        return self.rx_orientation_array

    def set_tx_lambertian_order_array(self, tx_lambertian_order_array):
        self.tx_lambertian_order_array = tx_lambertian_order_array
        self.set = True

    def get_tx_lambertian_order_array(self):
        return self.tx_lambertian_order_array

    def set_rx_photosensor_area_array(self, rx_photosensor_area_array):
        self.rx_photosensor_area_array = rx_photosensor_area_array
        self.set = True

    def get_rx_photosensor_area_array(self):
        return self.rx_photosensor_area_array

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

    def set_clip_neg(self, clip_neg):
        self.clip_neg = clip_neg

    def get_clip_neg(self):
        return self.clip_neg

    def set_shot_noise(self, shot_noise):
        self.shot_noise = shot_noise

    def get_shot_noise(self):
        return self.shot_noise

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_sample_rate(self):
        return self.sample_rate

    def set_responsivity(self, responsivity):
        self.responsivity = responsivity

    def get_responsivity(self):
        return self.responsivity

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

    def set_distance_array(self):
        self.distance_array = []
        for i in range(0, len(self.rx_coordinates_array), 3):
            rx_x, rx_y, rx_z = self.rx_coordinates_array[i:i + 3]
            for j in range(0, len(self.tx_coordinates_array), 3):
                tx_x, tx_y, tx_z = self.tx_coordinates_array[j:j + 3]
                distance = np.sqrt((rx_x - tx_x)**2 + (rx_y - tx_y)**2 + (rx_z - tx_z)**2)
                self.distance_array.append(distance)
        self.set = True


    def get_distance_array(self):
        return self.distance_array

    def set_emission_angle_array(self):
        self.emission_angle_array = []
        for i in range(0, len(self.rx_coordinates_array), 3):
            rx_x, rx_y, rx_z = self.rx_coordinates_array[i:i + 3]
            for j in range(0, len(self.tx_coordinates_array), 3):
                angle = 0
                tx_x, tx_y, tx_z = self.tx_coordinates_array[j:j + 3]
                u_vector = np.array([rx_x - tx_x, rx_y - tx_y, rx_z - tx_z])
                v_vector = np.array(self.tx_orientation_array[j:j + 3])
                u_mag = np.linalg.norm(u_vector)
                v_mag = np.linalg.norm(v_vector)
                if u_mag != 0:
                    cos_theta = np.dot(u_vector, v_vector) / (u_mag * v_mag)
                    cos_theta = np.clip(cos_theta, -1.0, 1.0)
                    angle = np.arccos(cos_theta) * (180 / np.pi)
                self.emission_angle_array.append(angle)
        self.set = True

    def get_emission_angle_array(self):
        return self.emission_angle_array

    def set_acceptance_angle_array(self):
        self.acceptance_angle_array = []
        for i in range(0, len(self.rx_coordinates_array), 3):
            rx_x, rx_y, rx_z = self.rx_coordinates_array[i:i + 3]
            v_vector = np.array(self.rx_orientation_array[i:i + 3])
            for j in range(0, len(self.tx_coordinates_array), 3):
                angle = 0
                tx_x, tx_y, tx_z = self.tx_coordinates_array[j:j + 3]
                u_vector = np.array([tx_x - rx_x, tx_y - rx_y, tx_z - rx_z])
                u_mag = np.linalg.norm(u_vector)
                v_mag = np.linalg.norm(v_vector)
                if u_mag != 0:
                    cos_theta = np.dot(u_vector, v_vector) / (u_mag * v_mag)
                    cos_theta = np.clip(cos_theta, -1.0, 1.0)
                    angle = np.arccos(cos_theta) * (180 / np.pi)
                self.acceptance_angle_array.append(angle)
        self.set = True

    def get_acceptance_angle_array(self):
        return self.acceptance_angle_array

    def calculate_channel_model_values(self):
        self.channel_model_values = []
        nout = self.get_num_outputs();
        nin = self.get_num_inputs();
        for x in range(nout):
            for j in range(nin):
                Gt = 0
                Gr = 0
                H = 1
                
                index = x * nin + j
                emission_angle = self.get_emission_angle_array()[index]
                acceptance_angle = self.get_acceptance_angle_array()[index]
                distance = self.get_distance_array()[index]
                lambertian_order = self.get_tx_lambertian_order_array()[j]
                photosensor_area = self.get_rx_photosensor_area_array()[x]
                optical_filter_transmittance = self.get_optical_filter_transmittance_array()[x]
                refractive_index = self.get_refractive_index_array()[x]
                concentrator_FOV = self.get_concentrator_FOV_array()[x]
                E2O_conversion_factor = self.get_E2O_conversion_factor_array()[j]
                O2E_conversion_factor = self.get_O2E_conversion_factor_array()[x]
                
                if distance != 0:
                    Gt = (lambertian_order + 1) / (2 * np.pi) * np.power(np.cos(np.radians(emission_angle)), lambertian_order) if emission_angle <= 90 else 0
                    Gr = photosensor_area * optical_filter_transmittance * (refractive_index ** 2 / np.sin(np.radians(concentrator_FOV)) ** 2) * np.cos(np.radians(acceptance_angle)) if acceptance_angle <= concentrator_FOV and acceptance_angle >= 0 else 0
                    H = E2O_conversion_factor * (Gt * Gr / (distance ** 2)) * O2E_conversion_factor if distance != 0 else 0
                
                self.channel_model_values.append(H)
        self.set = False

    def calculate_shot_noise(self, P_avg):
        q = 1.60217663e-19
        S_shot = 2 * q * self.get_responsivity() * P_avg
        variance = S_shot * self.get_sample_rate()
        std_dev = np.sqrt(variance)
        return std_dev


    def work(self, input_items, output_items):
        ninputs = len(input_items)
        noutputs = len(output_items)
        noutput_items = len(output_items[0])

        if self.set:
            self.set_distance_array()
            self.set_emission_angle_array()
            self.set_acceptance_angle_array()
            self.calculate_channel_model_values()
        
        power_sums = [0.0] * noutputs

        for x in range(noutputs):
            for i in range(noutput_items):
                received_power = 0.0
                for j in range(ninputs):
                    index = x * ninputs + j
                    in_item = input_items[j][i]
                    if self.get_clip_neg():
                        in_item = max(input_items[j][i], 0.0)  
                    received_power += in_item * self.channel_model_values[index]

                output_items[x][i] = received_power
                power_sums[x] += received_power
                
            if self.get_shot_noise():
                P_avg = np.abs(power_sums[x]) / noutput_items
                std_dev = self.calculate_shot_noise(P_avg)  

                for i in range(noutput_items):
                    noise_factor = np.random.normal(loc=0, scale=std_dev)  
                    output_items[x][i] += noise_factor  


        return len(output_items[0])
