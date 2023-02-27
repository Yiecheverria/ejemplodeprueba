package com.distribuida.config;

import com.datastax.oss.driver.api.core.CqlSession;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.enterprise.inject.Produces;
import jakarta.inject.Inject;
import org.eclipse.microprofile.config.inject.ConfigProperty;
import java.net.InetSocketAddress;
import java.net.SocketTimeoutException;


@ApplicationScoped
public class DatabaseConfig {

    @Inject
    @ConfigProperty(name = "cassandra.uri")
    private String cassandraUri;
    @Inject
    @ConfigProperty(name = "cassandra.port")
    private Integer cassandraPort;
    @Inject
    @ConfigProperty(name = "cassandra.datacenter")
    private  String datacenter;

    @Produces
    public CqlSession session(){
        System.out.printf(cassandraUri);
        System.out.println(cassandraPort);
        System.out.println(datacenter);
        InetSocketAddress contactPoint = new InetSocketAddress(cassandraUri, cassandraPort);
        System.out.println(contactPoint);
        return CqlSession.builder()
                .addContactPoint(contactPoint)
                .withLocalDatacenter(datacenter)
                .build();
    }


}
