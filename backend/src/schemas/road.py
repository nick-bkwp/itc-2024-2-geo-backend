from pydantic import BaseModel, Field

class AddRoadRequest(BaseModel):
    common_info: dict = Field(alias='common-info')
    road_owners: dict = Field(alias='road-owners')
    operating_organizations: dict = Field(alias='operating-organizations')
    regulations: dict = Field(alias='regulations')
    backbone_network: dict = Field(alias='backbone-network')
    start_exploraion: dict = Field(alias='start-exploraion')
    paid_section_of_the_road: dict = Field(alias='paid-section-of-the-road')
    dangerous_sections: dict = Field(alias='dangerous-sections')
    cross_subjects: dict = Field(alias='cross-subjects')
    climatic_zones: dict = Field(alias='climatic-zones')
    terrain_types: dict = Field(alias='terrain-types')
    max_speeds: dict = Field(alias='max-speeds')
    axle_loads: dict = Field(alias='axle-loads')
    traffic_intensities: dict = Field(alias='traffic-intensities')
    categories: dict = Field(alias='categories')
    road_class: dict = Field(alias='road-class')
    number_of_lanes: dict = Field(alias='number-of-lanes')
    roadway_width: dict = Field(alias='roadway-width')
    earthen_canvas_width: dict = Field(alias='earthen-canvas-width')
    type_of_coatings: dict = Field(alias='type-of-coatings')
    geodata: list[dict] = Field(alias='geodata')

class GetGeometriesResponse(BaseModel):
    common_info: dict = Field(serialization_alias='common-data')
    geodata: list[dict]
