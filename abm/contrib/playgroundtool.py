"""parameters for interactive playground simulations"""

default_params = {
                "N": 5,
                "T": 100000,
                "v_field_res": 1200,
                "width": 500,
                "height": 500,
                "framerate": 30,
                "window_pad": 30,
                "with_visualization": True,
                "show_vis_field": False,
                "show_vis_field_return": True,
                "pooling_time": 0,
                "pooling_prob":0,
                "agent_radius": 10,
                "N_resc": 3,
                "min_resc_perpatch": 200,
                "max_resc_perpatch": 201,
                "min_resc_quality": 0.25,
                "max_resc_quality": 0.25,
                "patch_radius": 30,
                "regenerate_patches": True,
                "agent_consumption": 1,
                "teleport_exploit": False,
                "vision_range": 5000,
                "agent_fov": 0.5,
                "visual_exclusion": True,
                "show_vision_range": True,
                "use_ifdb_logging": False,
                "save_csv_files": False,
                "ghost_mode": True,
                "patchwise_exclusion": True,
                "parallel": False
}

help_messages = {
    'framerate': '''
    
                    Framerate [fps]: 
    
                    The framerate is a parameter that defines how often 
                    (per second) is the state of the simulation is
                    updated. In case the simulation has many agents/resources 
                    it might happen that the requested
                    framerate is impossible to keep with the given hardware. 
                    In that case the maximal possible framerate
                    will be kept. 
    
    ''',
    'N':'''
    
                    Number of agents, N [pcs]: 
    
                    The number of agent controls how many individuals the
                    group consists of in terms of foraging agents visualized
                    as colorful circles with a white line showing their ori-
                    entations. The field of view of the agents are shown
                    with a green circle slice.
    
    ''',
    'N_res':'''
    
                    Number of resource patches, N_res [pcs]: 
    
                    The number of resource patches in the environment. 
                    Each resource patch can be exploited by agents and they
                    contain a given amount of resource units. The quality
                    of the patch controls how fast (unit/time) can be
                    the resource patch exploited by a single agent. Resource
                    patches are shown as gray circles on the screen.
    
    ''',
    'FOV': '''

                    Field of View, FOV [%]: 
    
                    The amount (in percent) of visible area around individual
                    agents. In case this is 0, the agents are blind. In case
                    it is 100, the agents have a full 360° FOV.

    ''',
    'RES': '''

                    Resource Radius, R [px]: 
    
                    The radius of resource patches in pixels. In case the overall
                    covered resource area on the arena exceeds 30% of the total space
                    the number of resource patches will be automatically decreased. 

    ''',
    'Epsw': '''

                    Social Excitability, E_w [a.U.]: 
        
                    The parameter controls how socially excitable agents are, i.e. how
                    much a unit of social information can increase/bias the decision
                    process of the agent towards socially guided behavior (Relocation).
                    In case this parameter is 0, agents do not integrate social cues
                    at all. The larger this parameter is, the faster individuals respond
                    to visible exploiting agents and the farther social cues are triggering
                    relocation movement.

    ''',
    'Epsu': '''

                    Individual Preference Factor, E_u [a.U.]: 
            
                    The parameter controls how much a unit of exploited resource biases
                    the agent towards further exploitation of resources.
                    In case this parameter is low, agents will get picky
                    with resource patches, i.e. they stop exploiting low-quality
                    patches after an initial sampling period.

    ''',
}