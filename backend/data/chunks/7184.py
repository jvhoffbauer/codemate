def payload_to_list(hpp: HousePredictionPayload) -> List:
    return [
        hpp.median_income_in_block,
        hpp.median_house_age_in_block,
        hpp.average_rooms,
        hpp.average_bedrooms,
        hpp.population_per_block,
        hpp.average_house_occupancy,
        hpp.block_latitude,
        hpp.block_longitude,
    ]