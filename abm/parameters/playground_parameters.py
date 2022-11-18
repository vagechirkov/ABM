from pydantic import BaseSettings


class PlaygroundEnvironmentParameters(BaseSettings):
    """Environment variables"""
    width: int = 500
    height: int = 500
    framerate: int = 30  # interactive
    window_pad: int = 30
    use_ram_logging: bool = False
    use_zarr: bool = True
    save_csv_files: bool = False
    parallel: bool = False
    allow_border_patch_overlap: bool = True


class PlaygroundUIParameters(BaseSettings):
    """Playground parameters"""
    with_visualization: bool = True
    show_vis_field: bool = False
    show_vis_field_return: bool = True
    show_vision_range: bool = True


class PlaygroundAgentParameters(BaseSettings):
    """Agent variables"""
    pooling_time: int = 0
    pooling_prob: int = 0
    agent_radius: int = 10
    agent_consumption: int = 1
    vision_range: int = 2000
    agent_fov: float = 1  # interactive
    visual_exclusion: bool = True  # interactive
    ghost_mode: bool = True  # interactive
    patchwise_exclusion: bool = True
    collide_agents: bool = False


class PlaygroundResourceParameters(BaseSettings):
    """Resource variables"""
    min_resc_perpatch: int = 200
    max_resc_perpatch: int = 201
    min_resc_quality: float = 0.25
    max_resc_quality: float = 0.25
    patch_radius: int = 15  # interactive
    regenerate_patches: bool = True
    teleport_exploit: bool = False


class PlaygroundParameters(BaseSettings):
    environment_parameters: PlaygroundEnvironmentParameters = \
        PlaygroundEnvironmentParameters()
    ui_parameters: PlaygroundUIParameters = PlaygroundUIParameters()
    agent_parameters: PlaygroundAgentParameters = \
        PlaygroundAgentParameters()
    resource_parameters: PlaygroundResourceParameters = \
        PlaygroundResourceParameters()