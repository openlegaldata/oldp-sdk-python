# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from oldp_client.api_client import ApiClient


class AnnotationLabelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def annotation_labels_create(self, data, **kwargs):  # noqa: E501
        """annotation_labels_create  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_create(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnnotationLabel data: (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.annotation_labels_create_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.annotation_labels_create_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def annotation_labels_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """annotation_labels_create  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_create_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnnotationLabel data: (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method annotation_labels_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `annotation_labels_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/annotation_labels/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationLabel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def annotation_labels_delete(self, id, **kwargs):  # noqa: E501
        """annotation_labels_delete  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.annotation_labels_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.annotation_labels_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def annotation_labels_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """annotation_labels_delete  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method annotation_labels_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `annotation_labels_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/annotation_labels/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def annotation_labels_list(self, **kwargs):  # noqa: E501
        """annotation_labels_list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ordering: Which field to use when ordering the results.
        :param float owner: 
        :param str slug: 
        :param str private: 
        :param str trusted: 
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.annotation_labels_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.annotation_labels_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def annotation_labels_list_with_http_info(self, **kwargs):  # noqa: E501
        """annotation_labels_list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ordering: Which field to use when ordering the results.
        :param float owner: 
        :param str slug: 
        :param str private: 
        :param str trusted: 
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ordering', 'owner', 'slug', 'private', 'trusted', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method annotation_labels_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ordering' in params:
            query_params.append(('ordering', params['ordering']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
        if 'slug' in params:
            query_params.append(('slug', params['slug']))  # noqa: E501
        if 'private' in params:
            query_params.append(('private', params['private']))  # noqa: E501
        if 'trusted' in params:
            query_params.append(('trusted', params['trusted']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/annotation_labels/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def annotation_labels_partial_update(self, id, data, **kwargs):  # noqa: E501
        """annotation_labels_partial_update  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_partial_update(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :param AnnotationLabel data: (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.annotation_labels_partial_update_with_http_info(id, data, **kwargs)  # noqa: E501
        else:
            (data) = self.annotation_labels_partial_update_with_http_info(id, data, **kwargs)  # noqa: E501
            return data

    def annotation_labels_partial_update_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """annotation_labels_partial_update  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_partial_update_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :param AnnotationLabel data: (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method annotation_labels_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `annotation_labels_partial_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `annotation_labels_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/annotation_labels/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationLabel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def annotation_labels_read(self, id, **kwargs):  # noqa: E501
        """annotation_labels_read  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.annotation_labels_read_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.annotation_labels_read_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def annotation_labels_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """annotation_labels_read  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method annotation_labels_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `annotation_labels_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/annotation_labels/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationLabel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def annotation_labels_update(self, id, data, **kwargs):  # noqa: E501
        """annotation_labels_update  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_update(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :param AnnotationLabel data: (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.annotation_labels_update_with_http_info(id, data, **kwargs)  # noqa: E501
        else:
            (data) = self.annotation_labels_update_with_http_info(id, data, **kwargs)  # noqa: E501
            return data

    def annotation_labels_update_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """annotation_labels_update  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.annotation_labels_update_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this Label. (required)
        :param AnnotationLabel data: (required)
        :return: AnnotationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method annotation_labels_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `annotation_labels_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `annotation_labels_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/annotation_labels/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationLabel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
