"""
작품 관련 유틸 함수들 (작품 및 회차/문단 관련 함수 포함)
"""
from typing import List, Any

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from app.schemas.series import Series


def get_sum_of_count(series: List[Series], category: str):
    if series:
        try:
            series_statistic_list = list(filter(lambda x: x is not None, [s.series_statistic for s in series]))
            count = sum([jsonable_encoder(series_statistic).get(category) for series_statistic in series_statistic_list])
            return count
        except:
            return 0
    else:
        return 0


def get_avg_rating(series: List[Series]):
    try:
        return round(get_sum_of_count(series=series, category="rating")/len(series), 1)
    except ZeroDivisionError:
        return 0


def get_meta_from_meta_list(meta_list: list, comparison: str, criteria: Any, value: str):
    """
    메타데이터 리스트에서 원하는 대조군과 그 결과값을 기반으로 메타데이터 dict에서 특정 key의 value를 꺼내옵니다.\n
    :param meta_list: 작품이나 회차의 메타정보 리스트 (series.series_meta 혹은 novel.novel_meta)\n
    :param comparison:  비교군 ("is_origin" 혹은 'language_code")\n
    :param criteria:  비교값 (is_origin > bool로 비교 // language_code > string으로 비교)\n
    :param value:  꺼내올 값 (title, description 등)\n
    :return: 꺼내온 값
    """
    if comparison == "is_origin" or comparison == "language_code":
        matched_list = list(filter(lambda x: x.get(comparison) == criteria, [meta for meta in jsonable_encoder(meta_list)]))
        if len(matched_list) < 1:
            raise HTTPException(status_code=404, detail="Can not found Anythings, Please check your parameters")
        return matched_list[0].get(value)
    raise HTTPException(status_code=404, detail="Can not found Anythings, Please check your parameters")
