    def _pre_process(self, payload: HousePredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result