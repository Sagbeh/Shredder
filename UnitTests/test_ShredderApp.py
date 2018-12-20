import unittest
from app import app


class shredderTestCase(unittest.TestCase):

    # ensure that registration page is set up correctly
    def test_registration(self):
        tester = app.test_client(self)
        response = tester.get('/registration', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure updatecore loads correctly
    def test_update_core(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/updatecore', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure updatelegs loads correctly
    def test_update_leg(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/updateleg', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure list loads correctly
    def test_admin_chat(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/chat', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure updatearms loads correctly
    def test_update_arms(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/updatearms', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure updatechestback loads correctly
    def test_update_chest_back(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/updatechestback', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewcore loads correctly
    def test_view_core(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/viewcore', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewlegs loads correctly
    def test_view_leg(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/viewleg', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure list loads correctly
    def test_list(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/list', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewarms loads correctly
    def test_view_arms(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/viewarms', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewchestback loads correctly
    def test_view_chest_back(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/chestback', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewcoreprogress loads correctly
    def test_view_core_progress(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/viewcore', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewlegsprogress loads correctly
    def test_view_leg_progress(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/viewleg', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure resources loads correctly
    def test_resources(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="test", password="test"), follow_redirects=True)
        response = tester.get('/resources', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewarmsprogress loads correctly
    def test_view_arms_progress(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="test", password="test"), follow_redirects=True)
        response = tester.get('/viewarmsprogress', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensure viewchestback loads correctly
    def test_chat_chest_back_progress(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="test", password="test"), follow_redirects=True)
        response = tester.get('/viewchestbackprogress', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    # ensure chat loads correctly
    def test_chat(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="test", password="test"), follow_redirects=True)
        response = tester.get('/chat', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #ensure that index page is set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)


    # ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Shredder App' in response.data)

    # ensure that login behaves correctly with correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="test", password="test"), follow_redirects=True)
        self.assertIn(b'Hello Test', response.data)

    # ensure that login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username = "wrong", password = "wrong"), follow_redirects = True)
        self.assertIn(b'Error:', response.data)


    # ensure that login behaves correctly with correct admin credentials
    def test_correct_admin_login(self):
        tester = app.test_client(self)
        response = tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        self.assertIn(b'You were successfully logged in', response.data)

    # ensure that login behaves correctly with incorrect admin credentials
    def test_incorrect_admin_login(self):
        tester = app.test_client(self)
        response = tester.post('/adminlogin', data=dict(username="wrong", password="wrong"), follow_redirects=True)
        self.assertIn(b'Error:', response.data)

    # ensure logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/adminlogin', data=dict(username="Shredder", password="admin"), follow_redirects=True)
        response = tester.get('/login', follow_redirects = True)
        self.assertIn(b'New User?', response.data)



if __name__ == '__main__':
    unittest.main()


