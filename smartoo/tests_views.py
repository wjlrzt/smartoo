# encoding=utf-8

from __future__ import unicode_literals

#from django.core.urlresolvers import reverse
from django.test import TestCase

from common.utils.mock import MockObject
from knowledge.namespaces import TERM
from knowledge.models import KnowledgeGraph
from smartoo.models import Session
from smartoo.views import build_knowledge

from json import loads


class StartSessionViewTestCase(TestCase):
    fixtures = ['fake-components-vertical.xml']

    def setUp(self):
        pass

    def test_start_session_successfully(self):
        response = self.client.post('/interface/start-session/Abraham_Lincoln')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(loads(response.content)["success"], True)
        sessions = Session.objects.all()
        self.assertEqual(len(sessions), 1)
        session = sessions[0]
        self.assertEqual(session.topic, TERM['Abraham_Lincoln'])

    def test_start_session_unsuccessfully(self):
        response = self.client.post('/interface/start-session/Some_nonsense')
        #self.assertEqual(response.status_code, 200)
        #print 'code', response.status_code
        self.assertEqual(loads(response.content)["success"], False)
        sessions = Session.objects.all()
        self.assertEqual(len(sessions), 0)

# NOTE: As it's problematic too test view using session data, we will test
# directly views methods using fake requests (with fake session dictionary)


class BuildKnowledgeViewTestCase(TestCase):
    fixtures = ['fake-components-vertical.xml']

    def test_build_knowledge(self):
        #response = self.client.post('/interface/build-knowledge')
        topic = TERM['Abraham_Lincoln']
        session = Session.objects.create_with_components(topic)
        fake_request = MockObject(session={'session_id': session.id})

        response = build_knowledge(fake_request)
        self.assertEqual(loads(response.content)["success"], True)
        self.assertEqual(response.status_code, 200)

        # check that the knowledge was built
        knowledge_graphs = KnowledgeGraph.objects.all()
        self.assertEqual(len(knowledge_graphs), 1)
        knowledge_graph = knowledge_graphs[0]
        self.assertEqual(knowledge_graph.topic, topic)

    def test_build_knowledge_invalid_term(self):
        topic = TERM['Some_nonsense']
        session = Session.objects.create_with_components(topic)
        fake_request = MockObject(session={'session_id': session.id})
        response = build_knowledge(fake_request)
        self.assertEqual(loads(response.content)["success"], False)
        knowledge_graphs = KnowledgeGraph.objects.all()
        self.assertEqual(len(knowledge_graphs), 0)

    def test_build_knowledge_invalid_session_id(self):
        topic = TERM['Abraham_Lincoln']
        session = Session.objects.create_with_components(topic)
        fake_request = MockObject(session={'session_id': session.id + 1})
        response = build_knowledge(fake_request)
        self.assertEqual(loads(response.content)["success"], False)
        knowledge_graphs = KnowledgeGraph.objects.all()
        self.assertEqual(len(knowledge_graphs), 0)

#def _session_storage_init(test_case):
#    """
#    Helper function to enable storing session for a test_case
#    NOTE: It  didn't work correctly...
#    """
#    settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
#    engine = import_module(settings.SESSION_ENGINE)
#    store = engine.SessionStore()
#    store.save()
#    test_case.session = store
#    test_case.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key